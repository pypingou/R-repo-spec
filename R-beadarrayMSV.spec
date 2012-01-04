%global packname  beadarrayMSV
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Analysis of Illumina BeadArray SNP data including MSV markers

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-methods R-geneplotter 

BuildRequires:    R-devel tex(latex) R-Biobase R-methods R-geneplotter 

%description
Imports bead-summary data from Illumina scanner. Pre-processes using a
suite of optional normalizations and transformations. Clusters and
automatically calls genotypes, critically able to handle markers in
duplicated regions of the genome (multisite variants; MSVs). Interactive
clustering if needed. MSVs with variation in both paralogs may be resolved
and mapped to their respective chromosomes. Quality control including
pedigree checking and visual assessment of clusters. Too large data-sets
are handled by working on smaller subsets of the data in sequence.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora