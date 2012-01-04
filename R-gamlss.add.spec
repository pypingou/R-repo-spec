%global packname  gamlss.add
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.0.5
Release:          1%{?dist}
Summary:          GAMLSS Additive.

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gamlss R-mgcv R-nnet R-gamlss.util R-gamlss.nl R-lattice 

BuildRequires:    R-devel tex(latex) R-gamlss R-mgcv R-nnet R-gamlss.util R-gamlss.nl R-lattice 

%description
Extra additive terms for GAMLSS models.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/gamlss.add/html
%doc %{rlibdir}/gamlss.add/DESCRIPTION
%{rlibdir}/gamlss.add/NAMESPACE
%{rlibdir}/gamlss.add/R
%{rlibdir}/gamlss.add/Meta
%{rlibdir}/gamlss.add/INDEX
%{rlibdir}/gamlss.add/help
%{rlibdir}/gamlss.add/LICENSE

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.0.5-1
- initial package for Fedora