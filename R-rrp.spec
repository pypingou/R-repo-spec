%global packname  rrp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.9
Release:          1%{?dist}
Summary:          Random Recursive Partitioning

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rpart 

BuildRequires:    R-devel tex(latex) R-rpart 

%description
Random Recursive Partitiong and Rank-based proximities for data matching,
missing data imputation and nonparametric classification and prediction

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
%doc %{rlibdir}/rrp/LICENCE
%doc %{rlibdir}/rrp/html
%doc %{rlibdir}/rrp/DESCRIPTION
%{rlibdir}/rrp/NAMESPACE
%{rlibdir}/rrp/Meta
%{rlibdir}/rrp/libs
%{rlibdir}/rrp/help
%{rlibdir}/rrp/R
%{rlibdir}/rrp/data
%{rlibdir}/rrp/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.9-1
- initial package for Fedora