%global packname  RMAGEML
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.28.0
Release:          1%{?dist}
Summary:          Handling MAGEML documents

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-marray R-limma R-Biobase 


BuildRequires:    R-devel tex(latex) R-methods R-marray R-limma R-Biobase



%description
This package can be used to handle MAGEML documents in Bioconductor

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.28.0-1
- initial package for Fedora