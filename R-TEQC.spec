%global packname  TEQC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Quality control for target capture experiments

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-IRanges R-Rsamtools R-hwriter 

BuildRequires:    R-devel tex(latex) R-IRanges R-Rsamtools R-hwriter 

%description
Target capture experiments combine hybridization-based (in solution or on
microarrays) capture and enrichment of genomic regions of interest (e.g.
the exome) with high throughput sequencing of the captured DNA fragments.
This package provides functionalities for assessing and visualizing the
quality of the target enrichment process, like specificity and sensitivity
of the capture, per-target read coverage and so on.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.0-1
- initial package for Fedora