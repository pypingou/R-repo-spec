%global packname  slam
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.23
Release:          1%{?dist}
Summary:          Sparse Lightweight Arrays and Matrices

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-23.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Data structures and algorithms for sparse arrays and matrices, based on
index arrays and simple triplet representations, respectively.

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
%doc %{rlibdir}/slam/DESCRIPTION
%doc %{rlibdir}/slam/html
%{rlibdir}/slam/help
%{rlibdir}/slam/INDEX
%{rlibdir}/slam/Meta
%{rlibdir}/slam/NAMESPACE
%{rlibdir}/slam/libs
%{rlibdir}/slam/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.23-1
- initial package for Fedora