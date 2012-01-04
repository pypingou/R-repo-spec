%global packname  tensor
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Tensor product of arrays

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The tensor product of two arrays is notionally an outer product of the
arrays collapsed in specific extents by summing along the appropriate

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
%doc %{rlibdir}/tensor/html
%doc %{rlibdir}/tensor/DESCRIPTION
%{rlibdir}/tensor/NAMESPACE
%{rlibdir}/tensor/help
%{rlibdir}/tensor/R
%{rlibdir}/tensor/Meta
%{rlibdir}/tensor/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora