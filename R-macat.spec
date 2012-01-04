%global packname  macat
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          MicroArray Chromosome Analysis Tool

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-annotate 


BuildRequires:    R-devel tex(latex) R-Biobase R-annotate



%description
This library contains functions to investigate links between differential
gene expression and the chromosomal localization of the genes. MACAT is
motivated by the common observation of phenomena involving large
chromosomal regions in tumor cells. MACAT is the implementation of a
statistical approach for identifying significantly differentially
expressed chromosome regions. The functions have been tested on a publicly
available data set about acute lymphoblastic leukemia (Yeoh et al.Cancer
Cell 2002), which is provided in the library 'stjudem'.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora