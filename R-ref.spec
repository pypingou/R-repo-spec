%global packname  ref
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.97
Release:          1%{?dist}
Summary:          References for R

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
small package with functions for creating references, reading from and
writing ro references and a memory efficient refdata type that
transparently encapsulates matrixes and data.frames

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
%doc %{rlibdir}/ref/html
%doc %{rlibdir}/ref/DESCRIPTION
%{rlibdir}/ref/exec
%{rlibdir}/ref/Meta
%{rlibdir}/ref/help
%{rlibdir}/ref/R
%{rlibdir}/ref/LICENSE
%{rlibdir}/ref/INDEX
%{rlibdir}/ref/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.97-1
- initial package for Fedora