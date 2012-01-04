%global packname  pdist
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Partitioned Distance Function

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Computes the euclidean distance between rows of a matrix X and rows of
another matrix Y.  Previously, this could only be done by binding the two
matrices together and calling 'dist', but this creates unnecessary
computation by computing the distances between a row of X and another row
of X, and likewise for Y.

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
%doc %{rlibdir}/pdist/DESCRIPTION
%doc %{rlibdir}/pdist/html
%{rlibdir}/pdist/libs
%{rlibdir}/pdist/help
%{rlibdir}/pdist/NAMESPACE
%{rlibdir}/pdist/Meta
%{rlibdir}/pdist/INDEX
%{rlibdir}/pdist/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora