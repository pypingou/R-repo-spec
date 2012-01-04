%global packname  ggtut
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.36
Release:          1%{?dist}
Summary:          support for tutorial on genetics of gene expression ISMB 2011

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-GGtools R-ff R-GenomicRanges R-snpStats R-GGdata R-GenomicFeatures R-ChIPpeakAnno R-Rsamtools R-cheung2010 R-SNPlocs.Hsapiens.dbSNP.20090506 R-hmyriB36 

BuildRequires:    R-devel tex(latex) R-GGtools R-ff R-GenomicRanges R-snpStats R-GGdata R-GenomicFeatures R-ChIPpeakAnno R-Rsamtools R-cheung2010 R-SNPlocs.Hsapiens.dbSNP.20090506 R-hmyriB36 

%description
various resources for genetics of expression with R/bioc

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.36-1
- initial package for Fedora