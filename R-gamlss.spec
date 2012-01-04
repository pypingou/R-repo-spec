%global packname  gamlss
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.1.1
Release:          1%{?dist}
Summary:          Generalized Additive Models for Location Scale and Shape.

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats R-splines R-utils R-gamlss.dist R-gamlss.data R-nlme 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-splines R-utils R-gamlss.dist R-gamlss.data R-nlme 

%description
The library for fitting GAMLSS models.

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.1.1-1
- initial package for Fedora