%global packname  nnclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Nearest-neighbour tools for clustering

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Finds nearest neighours and the minimum spanning tree for large data sets,
does clustering using the minimum spanning tree.

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
%doc %{rlibdir}/nnclust/DESCRIPTION
%doc %{rlibdir}/nnclust/doc
%doc %{rlibdir}/nnclust/html
%{rlibdir}/nnclust/NAMESPACE
%{rlibdir}/nnclust/Meta
%{rlibdir}/nnclust/R
%{rlibdir}/nnclust/libs
%{rlibdir}/nnclust/data
%{rlibdir}/nnclust/INDEX
%{rlibdir}/nnclust/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora