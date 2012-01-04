%global packname  gdsfmt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.5
Release:          1%{?dist}
Summary:          CoreArray Genomic Data Structure (GDS) R Interface

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
R interface of CoreArray GDS is based on the CoreArray project initiated
and developed by Xiuwen Zheng from 2007.

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
%doc %{rlibdir}/gdsfmt/DESCRIPTION
%doc %{rlibdir}/gdsfmt/html
%{rlibdir}/gdsfmt/NAMESPACE
%{rlibdir}/gdsfmt/INDEX
%{rlibdir}/gdsfmt/help
%{rlibdir}/gdsfmt/Meta
%{rlibdir}/gdsfmt/R
%{rlibdir}/gdsfmt/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.5-1
- initial package for Fedora