%global packname  metahdep
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Hierarchical Dependence in Meta-Analysis

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Tools for meta-analysis in the presence of hierarchical (and/or sampling)
dependence, including with gene expression studies

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
%doc %{rlibdir}/metahdep/doc
%doc %{rlibdir}/metahdep/DESCRIPTION
%doc %{rlibdir}/metahdep/html
%{rlibdir}/metahdep/help
%{rlibdir}/metahdep/Meta
%{rlibdir}/metahdep/libs
%{rlibdir}/metahdep/NAMESPACE
%{rlibdir}/metahdep/data
%{rlibdir}/metahdep/INDEX
%{rlibdir}/metahdep/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora