%global packname  vrmlgen
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.7
Release:          1%{?dist}
Summary:          Generate 3D visualizations for data exploration on the web

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
vrmlgen creates 3D scatter and bar plots, visualizations of 3D meshes,
parametric functions and height maps in web-formats like the Virtual
Reality Markup Language (VRML, filetype .wrl) and the LiveGraphics3D

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
%doc %{rlibdir}/vrmlgen/DESCRIPTION
%doc %{rlibdir}/vrmlgen/doc
%doc %{rlibdir}/vrmlgen/CITATION
%doc %{rlibdir}/vrmlgen/html
%{rlibdir}/vrmlgen/Meta
%{rlibdir}/vrmlgen/extdata
%{rlibdir}/vrmlgen/INDEX
%{rlibdir}/vrmlgen/NAMESPACE
%{rlibdir}/vrmlgen/help
%{rlibdir}/vrmlgen/data
%{rlibdir}/vrmlgen/R

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.7-1
- initial package for Fedora