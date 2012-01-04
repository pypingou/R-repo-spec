%global packname  rMAT
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.4.1
Release:          1%{?dist}
Summary:          R implementation from MAT program to normalize and analyze tiling arrays and ChIP-chip data.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-IRanges R-Biobase R-affxparser 
Requires:         R-Biobase R-methods R-IRanges 

BuildRequires:    R-devel tex(latex) R-IRanges R-Biobase R-affxparser
BuildRequires:    R-Biobase R-methods R-IRanges 


%description
This package is an R version of the package MAT and contains functions to
parse and merge Affymetrix BPMAP and CEL tiling array files (using C++
based Fusion SDK and Bioconductor package affxparser), normalize tiling
arrays using sequence specific models, detect enriched regions from
ChIP-chip experiments. Note: users should have GSL anf GenomeGraphs
installed. Windows users: 'consult the README file available in the inst
directory of the source distribution for necessary configuration
instructions'. Snow Leopard users can take advantage of increase speed
with Grand Central Dispatch!

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.4.1-1
- initial package for Fedora