%global packname  maxLik
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Maximum Likelihood Estimation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-miscTools 
Requires:         R-sandwich 

BuildRequires:    R-devel tex(latex) R-miscTools
BuildRequires:    R-sandwich 


%description
Tools for Maximum Likelihood Estimation

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
%doc %{rlibdir}/maxLik/NEWS
%doc %{rlibdir}/maxLik/DESCRIPTION
%doc %{rlibdir}/maxLik/html
%{rlibdir}/maxLik/Meta
%{rlibdir}/maxLik/INDEX
%{rlibdir}/maxLik/help
%{rlibdir}/maxLik/NAMESPACE
%{rlibdir}/maxLik/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora