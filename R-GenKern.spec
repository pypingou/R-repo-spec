%global packname  GenKern
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.10
Release:          1%{?dist}
Summary:          Functions for generating and manipulating binned kernel density estimates

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-KernSmooth R-utils 

BuildRequires:    R-devel tex(latex) R-KernSmooth R-utils 

%description
Computes generalised KDEs

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
%doc %{rlibdir}/GenKern/DESCRIPTION
%doc %{rlibdir}/GenKern/LICENCE
%doc %{rlibdir}/GenKern/html
%{rlibdir}/GenKern/help
%{rlibdir}/GenKern/INDEX
%{rlibdir}/GenKern/Meta
%{rlibdir}/GenKern/libs
%{rlibdir}/GenKern/R
%{rlibdir}/GenKern/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.10-1
- initial package for Fedora