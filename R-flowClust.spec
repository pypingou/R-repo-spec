%global packname  flowClust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.12.1
Release:          1%{?dist}
Summary:          Clustering for Flow Cytometry

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-mnormt R-ellipse R-Biobase R-flowCore 


BuildRequires:    R-devel tex(latex) R-methods R-mnormt R-ellipse R-Biobase R-flowCore



%description
Robust model-based clustering using a t-mixture model with Box-Cox
transformation. Note: users should have GSL installed. Windows users:
'consult the README file available in the inst directory of the source
distribution for necessary configuration instructions'.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.12.1-1
- initial package for Fedora