%global packname  proptest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Tests of the Proportional Hazards Assumption

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Tests of the proportional hazards assumption in the Cox model: data-driven
Neyman type smooth tests and score process based tests for identifying
nonproportional covariates and for global checks.

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
%doc %{rlibdir}/proptest/html
%doc %{rlibdir}/proptest/DESCRIPTION
%{rlibdir}/proptest/INDEX
%{rlibdir}/proptest/Meta
%{rlibdir}/proptest/help
%{rlibdir}/proptest/R
%{rlibdir}/proptest/libs
%{rlibdir}/proptest/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora