%global packname  CPE
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Concordance Probability Estimates in Survival Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-rms 


BuildRequires:    R-devel tex(latex) R-survival R-rms



%description
Functions to calculate concordance probability estimates in survival

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
%doc %{rlibdir}/CPE/html
%doc %{rlibdir}/CPE/DESCRIPTION
%{rlibdir}/CPE/Meta
%{rlibdir}/CPE/libs
%{rlibdir}/CPE/R
%{rlibdir}/CPE/NAMESPACE
%{rlibdir}/CPE/INDEX
%{rlibdir}/CPE/help
%{rlibdir}/CPE/demo

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.2-1
- initial package for Fedora