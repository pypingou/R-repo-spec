%global packname  urn
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Urn : Sampling Without Replacement

Group:            Applications/Engineering 
License:          AGPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions for sampling without replacement. (Simulated Urns).

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
%doc %{rlibdir}/urn/html
%doc %{rlibdir}/urn/DESCRIPTION
%doc %{rlibdir}/urn/CITATION
%{rlibdir}/urn/NAMESPACE
%{rlibdir}/urn/INDEX
%{rlibdir}/urn/Meta
%{rlibdir}/urn/help
%{rlibdir}/urn/LICENSE
%{rlibdir}/urn/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.1-1
- initial package for Fedora