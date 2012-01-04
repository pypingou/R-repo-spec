%global packname  aroma.core
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.2
Release:          1%{?dist}
Summary:          Core methods and classes used by aroma.* packages part of The Aroma Framework

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R.methodsS3 R-R.oo R-R.utils R-R.cache R-R.filesets R-R.rsp R-matrixStats R-digest R-aroma.light 
Requires:         R-affxparser R-RColorBrewer 

BuildRequires:    R-devel tex(latex) R-R.methodsS3 R-R.oo R-R.utils R-R.cache R-R.filesets R-R.rsp R-matrixStats R-digest R-aroma.light
BuildRequires:    R-affxparser R-RColorBrewer 


%description
This package contains core methods and classes used by higher-level
aroma.* packages part of the Aroma Project, e.g. aroma.affymetrix and
aroma.cn.  Its API should be considered to be in alpha and beta versions,
and is mostly of interest to developers.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.2-1
- initial package for Fedora