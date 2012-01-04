%global packname  parmigene
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Parallel Mutual Information estimation for Gene Network reconstruction.

Group:            Applications/Engineering 
License:          AGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package provides a parallel estimation of the mutual information based
on entropy estimates from k-nearest neighbors distances and algorithms for
the reconstruction of gene regulatory networks.

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
%doc %{rlibdir}/parmigene/DESCRIPTION
%doc %{rlibdir}/parmigene/html
%{rlibdir}/parmigene/R
%{rlibdir}/parmigene/INDEX
%{rlibdir}/parmigene/help
%{rlibdir}/parmigene/NAMESPACE
%{rlibdir}/parmigene/libs
%{rlibdir}/parmigene/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora