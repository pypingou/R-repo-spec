%global packname  altcdfenvs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.16.0
Release:          1%{?dist}
Summary:          alternative CDF environments (aka probeset mappings)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-affy R-makecdfenv R-Biostrings R-hypergraph 


BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-affy R-makecdfenv R-Biostrings R-hypergraph



%description
Convenience data structures and functions to handle cdfenvs

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.16.0-1
- initial package for Fedora