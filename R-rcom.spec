%global packname  rcom
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.3.1
Release:          1%{?dist}
Summary:          R COM Client Interface and internal COM Server

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-3.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rscproxy R-utils 


BuildRequires:    R-devel tex(latex) R-rscproxy R-utils



%description
R functions to interface with COM objects, R exposed to COM Clients

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.3.1-1
- initial package for Fedora