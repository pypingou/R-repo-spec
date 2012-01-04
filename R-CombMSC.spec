%global packname  CombMSC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Combined Model Selection Criteria

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions for computing optimal convex combinations of model selection
criteria based on ranks, along with utility functions for constructing
model lists, MSCs, and priors on model lists.

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
%doc %{rlibdir}/CombMSC/DESCRIPTION
%doc %{rlibdir}/CombMSC/html
%{rlibdir}/CombMSC/Meta
%{rlibdir}/CombMSC/INDEX
%{rlibdir}/CombMSC/R
%{rlibdir}/CombMSC/NAMESPACE
%{rlibdir}/CombMSC/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.2-1
- initial package for Fedora