%global packname  encoDnaseI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          data provided by UCSC for Cd4 raw measures of DnaseI hypersensitivity

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-lattice R-GGtools R-GGBase 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-lattice R-GGtools R-GGBase 

%description
data provided by UCSC for Cd4 raw measures of DnaseI hypersensitivity

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.9-1
- initial package for Fedora