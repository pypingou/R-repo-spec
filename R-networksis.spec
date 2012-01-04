%global packname  networksis
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Simulate bipartite graphs with fixed marginals through sequential importance sampling

Group:            Applications/Engineering 
License:          GPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ergm R-network 

BuildRequires:    R-devel tex(latex) R-ergm R-network 

%description
Tools to simulate bipartite networks/graphs with the degrees of the nodes
fixed and specified. Part of the "statnet" suite of packages for network

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
%doc %{rlibdir}/networksis/DESCRIPTION
%doc %{rlibdir}/networksis/CITATION
%doc %{rlibdir}/networksis/html
%{rlibdir}/networksis/Meta
%{rlibdir}/networksis/LICENSE
%{rlibdir}/networksis/libs
%{rlibdir}/networksis/data
%{rlibdir}/networksis/R
%{rlibdir}/networksis/NAMESPACE
%{rlibdir}/networksis/help
%{rlibdir}/networksis/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora