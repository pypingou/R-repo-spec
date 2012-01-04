%global packname  inlinedocs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.8
Release:          1%{?dist}
Summary:          Convert inline comments to documentation

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-utils 

%description
Generates Rd files from R source code with comments, providing for quick,
sustainable package development. The syntax keeps code and documentation
close together, and is inspired by the Don't Repeat Yourself principle.

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
%doc %{rlibdir}/inlinedocs/NEWS
%doc %{rlibdir}/inlinedocs/html
%doc %{rlibdir}/inlinedocs/DESCRIPTION
%{rlibdir}/inlinedocs/silly
%{rlibdir}/inlinedocs/INDEX
%{rlibdir}/inlinedocs/help
%{rlibdir}/inlinedocs/NAMESPACE
%{rlibdir}/inlinedocs/testfiles
%{rlibdir}/inlinedocs/R
%{rlibdir}/inlinedocs/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8-1
- initial package for Fedora