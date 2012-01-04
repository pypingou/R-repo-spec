%global packname  ggbio
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Static visualization for genomic data.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-biovizBase R-ggplot2 

BuildRequires:    R-devel tex(latex) R-methods R-biovizBase R-ggplot2 

%description
The ggbio package extends and specializes the grammar of graphics for
biological data. The graphics are designed to answer common scientific
questions, in particular those often asked of high throughput genomics
data. All core Bioconductor data structures are supported, where
appropriate. The package supports detailed views of particular genomic
regions, as well as genome-wide overviews. Supported overviews include
ideograms and grand linear views. High-level plots include sequence
fragment length, edge-linked interval to data view, mismatch pileup, and
several splicing summaries.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora