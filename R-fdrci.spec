%global packname  fdrci
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Permutation-based FDR Point and Confidence Interval Estimation

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
FDR functions for permutation-based estimators, including pi0 as well as
FDR confidence intervals. The confidence intervals account for
dependencies between tests by the incorporation of an overdispersion
parameter, which is estimated from the permuted data.

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
%doc %{rlibdir}/fdrci/DESCRIPTION
%doc %{rlibdir}/fdrci/html
%{rlibdir}/fdrci/INDEX
%{rlibdir}/fdrci/NAMESPACE
%{rlibdir}/fdrci/help
%{rlibdir}/fdrci/R
%{rlibdir}/fdrci/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora