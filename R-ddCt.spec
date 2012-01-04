%global packname  ddCt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          The ddCt Algorithm for the Analysis of Quantitative Real-Time PCR (qRT-PCR)

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-RColorBrewer R-xtable R-lattice R-methods 

BuildRequires:    R-devel tex(latex) R-Biobase R-RColorBrewer R-xtable R-lattice R-methods 

%description
The Delta-Delta-Ct (ddCt) Algorithm is an approximation method to
determine relative gene expression with quantitative real-time PCR
(qRT-PCR) experiments. Compared to other approaches, it requires no
standard curve for each primer-target pair, therefore reducing the working
load and yet returning accurate enough results as long as the assumptions
of the amplification efficiency hold. The ddCt package implements a
pipeline to collect, analyse and visualize qRT-PCR results, for example
those from TaqMan SDM software, mainly using the ddCt method. The pipeline
can be either invoked by a script in command-line or through the API
consisting of S4-Classes, methods and functions.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora