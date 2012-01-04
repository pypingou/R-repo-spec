%global packname  gpls
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Classification using generalized partial least squares

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Classification using generalized partial least squares for two-group and
multi-group (more than 2 group) classification.

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
%doc %{rlibdir}/gpls/html
%doc %{rlibdir}/gpls/doc
%doc %{rlibdir}/gpls/DESCRIPTION
%{rlibdir}/gpls/R
%{rlibdir}/gpls/help
%{rlibdir}/gpls/INDEX
%{rlibdir}/gpls/NAMESPACE
RPM build errors:
%{rlibdir}/gpls/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora