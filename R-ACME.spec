%global packname  ACME
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.10.0
Release:          1%{?dist}
Summary:          Algorithms for Calculating Microarray Enrichment (ACME)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-methods 
Requires:         R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-Biobase R-methods
BuildRequires:    R-graphics R-stats 


%description
ACME (Algorithms for Calculating Microarray Enrichment) is a set of tools
for analysing tiling array ChIP/chip, DNAse hypersensitivity, or other
experiments that result in regions of the genome showing "enrichment".  It
does not rely on a specific array technology (although the array should be
a "tiling" array), is very general (can be applied in experiments
resulting in regions of enrichment), and is very insensitive to array
noise or normalization methods.  It is also very fast and can be applied
on whole-genome tiling array experiments quite easily with enough memory.

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
%doc %{rlibdir}/ACME/html
%doc %{rlibdir}/ACME/doc
%doc %{rlibdir}/ACME/DESCRIPTION
%doc %{rlibdir}/ACME/CITATION
%{rlibdir}/ACME/extdata
%{rlibdir}/ACME/help
%{rlibdir}/ACME/INDEX
%{rlibdir}/ACME/data
%{rlibdir}/ACME/Meta
%{rlibdir}/ACME/R
%{rlibdir}/ACME/NAMESPACE
%{rlibdir}/ACME/libs

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.10.0-1
- initial package for Fedora