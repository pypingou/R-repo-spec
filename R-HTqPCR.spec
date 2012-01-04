%global packname  HTqPCR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Automated analysis of high-throughput qPCR data

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-RColorBrewer R-limma 
Requires:         R-affy R-Biobase R-gplots R-graphics R-grDevices R-limma R-methods R-RColorBrewer R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-Biobase R-RColorBrewer R-limma
BuildRequires:    R-affy R-Biobase R-gplots R-graphics R-grDevices R-limma R-methods R-RColorBrewer R-stats R-utils 


%description
Analysis of Ct values from high throughput quantitative real-time PCR
(qPCR) assays across multiple conditions or replicates. The input data can
be from spatially-defined formats such ABI TaqMan Low Density Arrays,
conventional 96- or 384-well plates, or microfluidic devices such as the
Dynamic Arrays from Fluidigm Corporation. HTqPCR handles data loading,
quality assessment, normalization, visualization and parametric or
non-parametric testing for statistical significance in Ct values between
features (e.g. genes, microRNAs).

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora