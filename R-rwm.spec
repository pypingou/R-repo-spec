%global packname  rwm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.53
Release:          1%{?dist}
Summary:          R Workspace Management

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
R workspace management functions. The principal functions are loadws,
attachws and savews. This packages provides a convenient method of
accessing with R workspaces that is OS independent. In simple situations,
it may replace the need for R packages.

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
%doc %{rlibdir}/rwm/DESCRIPTION
%doc %{rlibdir}/rwm/NEWS
%doc %{rlibdir}/rwm/doc
%doc %{rlibdir}/rwm/html
%{rlibdir}/rwm/Meta
%{rlibdir}/rwm/INDEX
%{rlibdir}/rwm/R
%{rlibdir}/rwm/NAMESPACE
%{rlibdir}/rwm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.53-1
- initial package for Fedora