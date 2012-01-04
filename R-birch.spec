%global packname  birch
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Dealing with very large datasets using BIRCH

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ellipse 

BuildRequires:    R-devel tex(latex) R-ellipse 

%description
birch is an implementation of the algorithms described in Zhang et al
(1997), and provides functions for creating CF-trees, along with
algorithms for dealing with some combinatorial problems, such as covMcd
and ltsReg. It is very well suited for dealing with very large data sets,
and does not require that the data can fit in physical memory.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora