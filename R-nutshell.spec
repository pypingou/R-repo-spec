%global packname  nutshell
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.02
Release:          1%{?dist}
Summary:          Data for "R in a Nutshell"

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains data sets used as examples in the book "R in a
Nutshell" from O'Reilly Media. For more information on this book, see

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
%doc %{rlibdir}/nutshell/html
%doc %{rlibdir}/nutshell/DESCRIPTION
%{rlibdir}/nutshell/extdata
%{rlibdir}/nutshell/NAMESPACE
%{rlibdir}/nutshell/help
%{rlibdir}/nutshell/LICENSE
%{rlibdir}/nutshell/INDEX
%{rlibdir}/nutshell/data
%{rlibdir}/nutshell/R
%{rlibdir}/nutshell/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.02-1
- initial package for Fedora