%global packname  polysat
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Tools for Polyploid Microsatellite Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-combinat R-methods 

BuildRequires:    R-devel tex(latex) R-combinat R-methods 

%description
polysat is a collection of tools to handle microsatellite data of any
ploidy (and samples of mixed ploidy) where allele copy number is not known
in partially heterozygous genotypes. It can import and export data in ABI
GeneMapper, Structure, ATetra, Tetrasat/Tetra, GenoDive, SPAGeDi, POPDIST,
and binary presence/absence formats.  It can calculate pairwise distances
between individuals using a stepwise mutation model or infinite alleles
model, with or without taking ploidies and allele frequencies into
account.  These distances can be used for the calculation of clonal
diversity statistics or used for further analysis in R.  polysat can also
assist the user in estimating the ploidy of samples, and lastly it can
estimate allele frequencies in populations, calculate pairwise Fst values
based on those frequencies, and export allele frequencies to SPAGeDi and

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora