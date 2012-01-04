%global packname  LifeTables
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          A package to implement HMD model life table system

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mclust 


BuildRequires:    R-devel tex(latex) R-mclust



%description
Functions supplied in this package will implement discriminant analysis to
select an appropriate life table family, select an appropriate alpha level
based on a desired life expectancy at birth, produce a model mortality
pattern based on family and level as well as plot the results.

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
%doc %{rlibdir}/LifeTables/DESCRIPTION
%doc %{rlibdir}/LifeTables/html
%{rlibdir}/LifeTables/data
%{rlibdir}/LifeTables/R
%{rlibdir}/LifeTables/Meta
%{rlibdir}/LifeTables/NAMESPACE
%{rlibdir}/LifeTables/help
%{rlibdir}/LifeTables/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora