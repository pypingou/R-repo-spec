%global packname  latdiag
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Draws diagrams useful for checking latent scales

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Writes a file of commands for the dot program to draw a graph proposed by
Rosenbaum and useful for checking some properties of various sorts of
latent scale

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
%doc %{rlibdir}/latdiag/DESCRIPTION
%doc %{rlibdir}/latdiag/CITATION
%doc %{rlibdir}/latdiag/doc
%doc %{rlibdir}/latdiag/html
%{rlibdir}/latdiag/R
%{rlibdir}/latdiag/NAMESPACE
%{rlibdir}/latdiag/help
%{rlibdir}/latdiag/INDEX
%{rlibdir}/latdiag/Meta

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora