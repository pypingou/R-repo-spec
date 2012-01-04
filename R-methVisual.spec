%global packname  methVisual
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Methods for visualization and statistics on DNA methylation data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biostrings R-plotrix R-gsubfn R-grid R-sqldf 
Requires:         R-Biostrings R-ca R-graphics R-grDevices R-grid R-gridBase R-IRanges R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-Biostrings R-plotrix R-gsubfn R-grid R-sqldf
BuildRequires:    R-Biostrings R-ca R-graphics R-grDevices R-grid R-gridBase R-IRanges R-stats R-utils 


%description
The package 'methVisual' allows the visualization of DNA methylation data
after bisulfite sequencing.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora