%global packname  MotIV
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.1
Release:          1%{?dist}
Summary:          Motif Identification and Validation

Group:            Applications/Engineering 
License:          GPL 2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-graphics R-grid R-IRanges R-lattice R-methods R-rGADEM R-stats R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-graphics R-grid R-IRanges R-lattice R-methods R-rGADEM R-stats R-utils 


%description
This package makes use of STAMP for comparing a set of motifs to a given
database (e.g. JASPAR). It can also be used to visualize motifs, motif
distributions, modules and filter motifs.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.1-1
- initial package for Fedora