%global packname  modelcf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Modeling physical computer codes with functional outputs using clustering and dimensionality reduction

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Statistical learning with vectorial inputs and smooth 1D curves as
outputs. The main function builds a model from n samples (x_i,y_i).

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
%doc %{rlibdir}/modelcf/html
%doc %{rlibdir}/modelcf/DESCRIPTION
%doc %{rlibdir}/modelcf/doc
%{rlibdir}/modelcf/NAMESPACE
%{rlibdir}/modelcf/Meta
%{rlibdir}/modelcf/libs
%{rlibdir}/modelcf/help
%{rlibdir}/modelcf/R
%{rlibdir}/modelcf/data
%{rlibdir}/modelcf/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora