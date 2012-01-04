%global packname  enrichvs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Enrichment assessment of virtual screening approaches

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
These programs are used for calculating enrichment factors, drawing
enrichment curves to evaluate virtual screening approaches.

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
%doc %{rlibdir}/enrichvs/html
%doc %{rlibdir}/enrichvs/DESCRIPTION
%{rlibdir}/enrichvs/help
%{rlibdir}/enrichvs/INDEX
%{rlibdir}/enrichvs/data
%{rlibdir}/enrichvs/Meta
%{rlibdir}/enrichvs/R
%{rlibdir}/enrichvs/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.5-1
- initial package for Fedora