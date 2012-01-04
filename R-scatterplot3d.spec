%global packname  scatterplot3d
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.33
Release:          1%{?dist}
Summary:          3D Scatter Plot

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-33.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Plots a three dimensional (3D) point cloud.

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
%doc %{rlibdir}/scatterplot3d/html
%doc %{rlibdir}/scatterplot3d/DESCRIPTION
%doc %{rlibdir}/scatterplot3d/CITATION
%doc %{rlibdir}/scatterplot3d/doc
%{rlibdir}/scatterplot3d/NAMESPACE
%{rlibdir}/scatterplot3d/R
%{rlibdir}/scatterplot3d/INDEX
%{rlibdir}/scatterplot3d/po
%{rlibdir}/scatterplot3d/Meta
%{rlibdir}/scatterplot3d/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.33-1
- initial package for Fedora