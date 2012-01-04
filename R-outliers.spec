%global packname  outliers
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.14
Release:          1%{?dist}
Summary:          Tests for outliers

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A collection of some tests commonly used for identifying outliers.

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
%doc %{rlibdir}/outliers/html
%doc %{rlibdir}/outliers/DESCRIPTION
%{rlibdir}/outliers/Meta
%{rlibdir}/outliers/INDEX
%{rlibdir}/outliers/R
%{rlibdir}/outliers/NAMESPACE
%{rlibdir}/outliers/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.14-1
- initial package for Fedora