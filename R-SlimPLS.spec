%global packname  SlimPLS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          SlimPLS multivariate feature selection

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-e1071 R-randomForest R-methods R-bioDist R-zipfR 

BuildRequires:    R-devel tex(latex) R-e1071 R-randomForest R-methods R-bioDist R-zipfR 

%description
SlimPLS is an implementation of SlimPLS multivariate feature selection.

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
%doc %{rlibdir}/SlimPLS/html
%doc %{rlibdir}/SlimPLS/DESCRIPTION
%{rlibdir}/SlimPLS/Meta
%{rlibdir}/SlimPLS/INDEX
%{rlibdir}/SlimPLS/R
%{rlibdir}/SlimPLS/NAMESPACE
%{rlibdir}/SlimPLS/help

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora