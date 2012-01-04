%global packname  FNN
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Fast Nearest Neighbor Search Algorithms and Applications

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A collection of fast k-nearest neighbor search algorithms and applications
including a cover-tree, kd-tree and the nearest neighbor algorithm in
package class. In addition, KNN classification, regression and information
measures are also implemented.

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
%doc %{rlibdir}/FNN/doc
%doc %{rlibdir}/FNN/html
%doc %{rlibdir}/FNN/DESCRIPTION
%{rlibdir}/FNN/R
%{rlibdir}/FNN/help
%{rlibdir}/FNN/INDEX
%{rlibdir}/FNN/libs
%{rlibdir}/FNN/NAMESPACE
RPM build errors:
%{rlibdir}/FNN/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.2-1
- initial package for Fedora