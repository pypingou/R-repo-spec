%global packname  EBarrays
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.18.0
Release:          1%{?dist}
Summary:          Unified Approach for Simultaneous Gene Clustering and Differential Expression Identification

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-lattice R-methods 

BuildRequires:    R-devel tex(latex) R-Biobase R-lattice R-methods 

%description
EBarrays provides tools for the analysis of replicated/unreplicated
microarray data.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.18.0-1
- initial package for Fedora