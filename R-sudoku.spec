%global packname  sudoku
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Sudoku Puzzle Generator and Solver

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Generates, plays, and solves Sudoku puzzles. The GUI playSudoku() needs
package "tkrplot" if you are not on Windows.

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
%doc %{rlibdir}/sudoku/html
%doc %{rlibdir}/sudoku/DESCRIPTION
%{rlibdir}/sudoku/INDEX
%{rlibdir}/sudoku/Meta
%{rlibdir}/sudoku/R
%{rlibdir}/sudoku/puz1.txt
%{rlibdir}/sudoku/puz2.txt
%{rlibdir}/sudoku/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora