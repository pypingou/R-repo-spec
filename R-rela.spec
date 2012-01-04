%global packname  rela
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.1
Release:          1%{?dist}
Summary:          Item Analysis Package with Standard Errors

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Item analysis with alpha standard error and principal axis factoring for
continuous variable scales (with plots).

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
%doc %{rlibdir}/rela/html
%doc %{rlibdir}/rela/DESCRIPTION
%doc %{rlibdir}/rela/CITATION
%{rlibdir}/rela/help
%{rlibdir}/rela/Meta
%{rlibdir}/rela/R
%{rlibdir}/rela/INDEX
%{rlibdir}/rela/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.1-1
- initial package for Fedora