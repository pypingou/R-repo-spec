%global packname  GWASTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          GWASTools: Tools for Genome Wide Association Studies

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-ncdf R-GWASExactHW R-sandwich 
Requires:         R-methods R-DBI R-RSQLite R-DNAcopy R-survival 

BuildRequires:    R-devel tex(latex) R-Biobase R-ncdf R-GWASExactHW R-sandwich
BuildRequires:    R-methods R-DBI R-RSQLite R-DNAcopy R-survival 


%description
Classes for storing very large GWAS data sets and annotation, and
functions for GWAS data cleaning and analysis.

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora